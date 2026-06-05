import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from src.huffman import HuffmanCoding


st.set_page_config(
    page_title="Huffman Compression Utility",
    layout="wide"
)

st.title("🚀 Huffman Compression Visualizer")

st.markdown("DSA Project | Huffman Coding | File Compression Simulator")

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])


# =========================
# TREE VISUALIZATION
# =========================
def build_graph(node, graph, parent=None):
    if not node:
        return

    label = f"{node.char}:{node.freq}" if node.char else str(node.freq)

    graph.add_node(id(node), label=label)

    if parent:
        graph.add_edge(id(parent), id(node))

    build_graph(node.left, graph, node)
    build_graph(node.right, graph, node)


def draw_tree(root):
    G = nx.DiGraph()
    build_graph(root, G)

    pos = nx.spring_layout(G, seed=42)

    labels = nx.get_node_attributes(G, "label")

    plt.figure(figsize=(10, 6))
    nx.draw(
        G,
        pos,
        labels=labels,
        node_size=2000,
        node_color="lightblue",
        font_size=8,
        arrows=False
    )

    st.pyplot(plt)


# =========================
# MAIN APP
# =========================
if uploaded_file:

    text = uploaded_file.read().decode()

    h = HuffmanCoding()

    compressed, codes = h.compress(text)
    decompressed = h.decompress(compressed)

    freq = h.calculate_frequency(text)
    heap = h.build_heap(freq)
    root = h.build_tree(heap)

    original_bits = len(text) * 8
    compressed_bits = len(compressed)
    saved = ((original_bits - compressed_bits) / original_bits) * 100

    col1, col2, col3 = st.columns(3)

    col1.metric("Original Size", f"{original_bits} bits")
    col2.metric("Compressed Size", f"{compressed_bits} bits")
    col3.metric("Space Saved", f"{saved:.2f}%")

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Input", "Codes", "Tree", "Compressed", "Verify"]
    )

    with tab1:
        st.text_area("Input Text", text, height=300)

    with tab2:
        df = pd.DataFrame(list(codes.items()), columns=["Char", "Code"])
        st.dataframe(df, use_container_width=True)

    with tab3:
        st.subheader("Huffman Tree")
        draw_tree(root)

    with tab4:
        st.text_area("Compressed Data", compressed, height=300)

        st.download_button(
            "Download File",
            compressed,
            file_name="compressed.txt"
        )

    with tab5:
        if text == decompressed:
            st.success("Compression & Decompression Successful")
        else:
            st.error("Mismatch Error")

        st.text_area("Decompressed Text", decompressed, height=300)

else:
    st.info("Upload a file to begin")