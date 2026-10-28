```python
import streamlit as st
from pathlib import Path
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FileFlow - File Manager",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #f5f7fb;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Header */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    /* Cards */
    .card {
        background: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }

    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }

    .stat-number {
        font-size: 30px;
        font-weight: 800;
        color: #2563eb;
    }

    .stat-label {
        color: #6b7280;
        font-size: 14px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        padding: 10px 18px;
        border: none;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        padding: 30px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- FILE DIRECTORY ----------------
FILE_DIR = Path("files")
FILE_DIR.mkdir(exist_ok=True)


# ---------------- HELPER FUNCTIONS ----------------

def get_files():
    """Return all files from the files directory."""
    return sorted(
        [file for file in FILE_DIR.iterdir() if file.is_file()],
        key=lambda x: x.name.lower()
    )


def create_file(filename, content):
    try:
        path = FILE_DIR / filename

        if path.exists():
            return False, "File already exists."

        path.write_text(content, encoding="utf-8")
        return True, "File created successfully."

    except Exception as e:
        return False, str(e)


def read_file(filename):
    try:
        path = FILE_DIR / filename

        if not path.exists():
            return None, "File does not exist."

        return path.read_text(encoding="utf-8"), None

    except Exception as e:
        return None, str(e)


def append_file(filename, content):
    try:
        path = FILE_DIR / filename

        with open(path, "a", encoding="utf-8") as file:
            file.write("\n" + content)

        return True, "Content appended successfully."

    except Exception as e:
        return False, str(e)


def overwrite_file(filename, content):
    try:
        path = FILE_DIR / filename

        path.write_text(content, encoding="utf-8")

        return True, "File overwritten successfully."

    except Exception as e:
        return False, str(e)


def rename_file(old_name, new_name):
    try:
        old_path = FILE_DIR / old_name
        new_path = FILE_DIR / new_name

        if new_path.exists():
            return False, "A file with this name already exists."

        old_path.rename(new_path)

        return True, "File renamed successfully."

    except Exception as e:
        return False, str(e)


def delete_file(filename):
    try:
        path = FILE_DIR / filename

        if not path.exists():
            return False, "File does not exist."

        path.unlink()

        return True, "File deleted successfully."

    except Exception as e:
        return False, str(e)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 📁 FileFlow")

    st.markdown(
        "<p style='color:#9ca3af;'>Smart File Management System</p>",
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "➕ Create File",
            "📖 Read File",
            "✏️ Update File",
            "🗑️ Delete File"
        ]
    )

    st.divider()

    st.markdown("### 🛠️ Technologies")

    st.markdown("""
    **Python**  
    **Streamlit**  
    **Pathlib**  
    **File Handling**
    """)

    st.divider()

    st.caption("Developed as a Python File Handling Project")


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">📁 FileFlow</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A modern Python File Handling Management System</div>',
    unsafe_allow_html=True
)


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    files = get_files()

    txt_files = len([f for f in files if f.suffix == ".txt"])
    total_size = sum(f.stat().st_size for f in files)

    # Statistics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{len(files)}</div>
                <div class="stat-label">Total Files</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{txt_files}</div>
                <div class="stat-label">Text Files</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{total_size}</div>
                <div class="stat-label">Storage (Bytes)</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">CRUD</div>
                <div class="stat-label">Operations</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # Recent files
    st.markdown("### 📂 Your Files")

    if files:

        for file in files:

            col1, col2, col3 = st.columns([4, 2, 1])

            with col1:
                st.write(f"📄 **{file.name}**")

            with col2:
                size = file.stat().st_size
                st.write(f"{size} bytes")

            with col3:
                st.write(file.suffix or "File")

    else:

        st.info(
            "No files found. Create your first file using the Create File section."
        )


# =========================================================
# CREATE FILE
# =========================================================

elif page == "➕ Create File":

    st.markdown("### ➕ Create a New File")

    st.markdown(
        '<div class="card">Create a new text file and add content to it.</div>',
        unsafe_allow_html=True
    )

    filename = st.text_input(
        "File Name",
        placeholder="example.txt"
    )

    content = st.text_area(
        "File Content",
        placeholder="Write something here...",
        height=250
    )

    if st.button("🚀 Create File", use_container_width=True):

        if not filename:
            st.warning("Please enter a file name.")

        elif not filename.endswith(".txt"):
            st.warning("Please use a .txt file extension.")

        else:

            success, message = create_file(filename, content)

            if success:
                st.success(message)
                st.balloons()
                time.sleep(0.5)
                st.rerun()

            else:
                st.error(message)


# =========================================================
# READ FILE
# =========================================================

elif page == "📖 Read File":

    st.markdown("### 📖 Read File")

    files = get_files()

    if not files:

        st.info("No files available. Create a file first.")

    else:

        selected = st.selectbox(
            "Select a file",
            [file.name for file in files]
        )

        content, error = read_file(selected)

        if error:
            st.error(error)

        else:

            st.markdown("#### 📄 File Preview")

            st.code(
                content,
                language="text"
            )

            st.download_button(
                label="⬇️ Download File",
                data=content,
                file_name=selected,
                mime="text/plain",
                use_container_width=True
            )


# =========================================================
# UPDATE FILE
# =========================================================

elif page == "✏️ Update File":

    st.markdown("### ✏️ Update File")

    files = get_files()

    if not files:

        st.info("No files available.")

    else:

        selected = st.selectbox(
            "Select a file",
            [file.name for file in files]
        )

        operation = st.radio(
            "Choose Operation",
            [
                "📝 Append Content",
                "🔄 Overwrite File",
                "✏️ Rename File"
            ],
            horizontal=True
        )

        st.write("")

        # APPEND
        if operation == "📝 Append Content":

            content = st.text_area(
                "Content to Append",
                height=200
            )

            if st.button(
                "➕ Append Content",
                use_container_width=True
            ):

                if not content:
                    st.warning("Please enter some content.")

                else:

                    success, message = append_file(
                        selected,
                        content
                    )

                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)

        # OVERWRITE
        elif operation == "🔄 Overwrite File":

            content = st.text_area(
                "New File Content",
                height=250
            )

            st.warning(
                "⚠️ Overwriting will replace the existing content."
            )

            if st.button(
                "🔄 Overwrite File",
                use_container_width=True
            ):

                success, message = overwrite_file(
                    selected,
                    content
                )

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

        # RENAME
        else:

            new_name = st.text_input(
                "New File Name",
                placeholder="newname.txt"
            )

            if st.button(
                "✏️ Rename File",
                use_container_width=True
            ):

                if not new_name:
                    st.warning("Please enter a new file name.")

                else:

                    success, message = rename_file(
                        selected,
                        new_name
                    )

                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)


# =========================================================
# DELETE FILE
# =========================================================

elif page == "🗑️ Delete File":

    st.markdown("### 🗑️ Delete File")

    files = get_files()

    if not files:

        st.info("No files available.")

    else:

        selected = st.selectbox(
            "Select file to delete",
            [file.name for file in files]
        )

        st.error(
            f"⚠️ You are about to delete **{selected}**."
        )

        confirm = st.checkbox(
            "I understand that this action cannot be undone."
        )

        if st.button(
            "🗑️ Delete File",
            use_container_width=True
        ):

            if not confirm:
                st.warning(
                    "Please confirm the deletion first."
                )

            else:

                success, message = delete_file(selected)

                if success:
                    st.success(message)
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error(message)


# ---------------- FOOTER ----------------

st.markdown(
    """
    <div class="footer">
        Built with ❤️ using Python & Streamlit
        <br>
        FileFlow — Python File Handling Project
    </div>
    """,
    unsafe_allow_html=True
)
```
