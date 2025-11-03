from src.storage import save_post, load_posts

def add_post(text):
    save_post(text)
    print("Post added!")

def read_posts():
    posts = load_posts()
    if not posts:
        print("No posts yet.")
        return
    print("\nYour Posts:")
    for i, post in enumerate(posts, 1):
        print(f"{i}. {post.strip()}")
