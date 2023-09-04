import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import markdown
from bs4 import BeautifulSoup

def update_preview(event=None):
    markdown_text = text_editor.get(1.0, tk.END)
    html_text = markdown.markdown(markdown_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    formatted_html = soup.prettify()
    preview_text.config(state=tk.NORMAL)
    preview_text.delete(1.0, tk.END)
    preview_text.insert(tk.END, formatted_html)
    preview_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Markdown编辑器")

text_editor = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=60)
text_editor.pack(fill=tk.BOTH, expand=True)
text_editor.bind("<KeyRelease>", update_preview)  # 绑定键盘释放事件

preview_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=60)
preview_text.pack(fill=tk.BOTH, expand=True)
preview_text.config(state=tk.DISABLED)

root.mainloop()
