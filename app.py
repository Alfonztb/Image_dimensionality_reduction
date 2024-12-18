import streamlit as st
import os
from PIL import Image

# App Configuration
st.set_page_config(
    page_title="MNIST Dimensionality Reduction Guide",
    page_icon="🖼️",
    layout="wide"
)

# Visualization Directory
output_dir = "visualizations"

# Title and Description
st.markdown("""
# 🖼️ MNIST Dimensionality Reduction Guide  
Explore **PCA** and **t-SNE** for analyzing high-dimensional MNIST image data.  
This step-by-step guide walks through visualizations, variance analysis, and reconstructions.
""")

st.markdown("---")

# Step-by-Step Expandable Sections
with st.expander("📌 Step 1: Introduction"):
    st.write("""
MNIST is a dataset of handwritten digits represented as 28x28 pixel images.  
High-dimensional data (784 features per image) is challenging to analyze directly.  
Dimensionality reduction techniques, such as **PCA** and **t-SNE**, simplify the data while retaining its core structure.
""")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png", caption="Sample MNIST Digits", use_container_width=True)

# Visualizations Section
with st.expander("🎨 Step 2: Visualizing Reduced Data"):
    st.subheader("PCA Visualization (2D Projection)")
    pca_image_path = os.path.join(output_dir, "pca_visualization.png")
    if os.path.exists(pca_image_path):
        st.image(Image.open(pca_image_path), caption="PCA: Reduced to 2D", use_container_width=True)
    else:
        st.warning("PCA visualization image not found!")

    st.write("""
PCA reduces the dataset to **two principal components**.  
This 2D visualization highlights the separation between different digit clusters.
""")

    st.subheader("t-SNE Visualization (2D Projection)")
    tsne_image_path = os.path.join(output_dir, "tsne_visualization.png")
    if os.path.exists(tsne_image_path):
        st.image(Image.open(tsne_image_path), caption="t-SNE: Reduced to 2D", use_container_width=True)
    else:
        st.warning("t-SNE visualization image not found!")

    st.write("""
t-SNE captures **non-linear relationships** in the data, producing clearer clusters compared to PCA.
""")

# Trade-Off Section
with st.expander("⚖️ Step 3: Trade-Off Analysis"):
    st.subheader("Cumulative Explained Variance (PCA)")
    variance_plot_path = os.path.join(output_dir, "variance_plot.png")
    if os.path.exists(variance_plot_path):
        st.image(Image.open(variance_plot_path), caption="Cumulative Explained Variance", use_container_width=True)
    else:
        st.warning("Variance plot image not found!")

    variance_text_path = os.path.join(output_dir, "variance_analysis.txt")
    if os.path.exists(variance_text_path):
        st.subheader("Key Statistics")
        with open(variance_text_path, "r") as f:
            variance_content = f.read()
        st.text(variance_content)
    else:
        st.warning("Variance analysis text not found!")

    st.write("""
### Insights:
- Fewer components mean faster computations but lower information retention.
- More components retain more information but increase computational cost.
""")

# Reconstruction Section
with st.expander("🔄 Step 4: Original vs Reconstructed Images"):
    st.subheader("Original vs Reconstructed Images")
    reconstruction_image_path = os.path.join(output_dir, "reconstruction_comparison.png")
    if os.path.exists(reconstruction_image_path):
        st.image(Image.open(reconstruction_image_path), caption="Original (Top) vs Reconstructed (Bottom)", use_container_width=True)
    else:
        st.warning("Reconstruction comparison image not found!")

    st.write("""
Using **PCA with 100 components**, we approximate the original images.  
While details are slightly lost, the overall structure of the digits is retained.
""")

# Conclusion Section
with st.expander("✅ Step 5: Conclusion"):
    st.write("""
### Key Takeaways:
1. **PCA** is effective for linear dimensionality reduction and image reconstruction.
2. **t-SNE** provides powerful visualizations for non-linear patterns in data.
3. Balancing **information retention** and **computational efficiency** is critical.

Dimensionality reduction enables efficient analysis of high-dimensional datasets like MNIST, making it easier to visualize, process, and understand data.

---
Thank you for exploring this guide! 🚀
""")

# Footer
st.markdown("---")
st.markdown("🎓 **Created with Streamlit | MNIST Dataset Analysis**")
