"""三角関数インタラクティブ教材（単位円と波）を表示するStreamlitアプリ。

教材本体は同じフォルダの index.html（HTML + JavaScript）です。
このファイルは、それを読み込んで表示するだけの薄いラッパーです。
"""

from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="三角関数の周期性と単位円（JS高速版）",
    page_icon="📐",
    layout="wide",
)

HTML_PATH = Path(__file__).parent / "index.html"

# iframeの高さ（px）。ボタンが折り返す狭い画面で下が切れる場合は大きくしてください。
APP_HEIGHT = 1250


def render_html(html: str, height: int) -> None:
    """HTMLをiframeで表示する。

    st.components.v1.html は Streamlit 1.56 で非推奨になったため、
    新しい版では st.iframe を使い、古い版では components.html に切り替える。
    """
    if hasattr(st, "iframe"):
        st.iframe(html, height=height)
    else:
        import streamlit.components.v1 as components

        components.html(html, height=height, scrolling=False)


if not HTML_PATH.exists():
    st.error(
        "`index.html` が見つかりません。`streamlit_app.py` と同じフォルダに"
        "置いてください。"
    )
    st.stop()

render_html(HTML_PATH.read_text(encoding="utf-8"), APP_HEIGHT)
