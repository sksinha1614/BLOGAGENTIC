from src.states.blogstate import BlogState

# src/nodes/blog_node.py
class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        prompt = f"""
        You are an expert blog writer.
        Generate a creative, SEO-friendly title for:
        {state['topic']}
        """
        response = self.llm.invoke(prompt)
        return {
            "blog": {
                "title": response.content,
                "content": ""
            }
        }

    def content_generation(self, state: BlogState):
        prompt = f"""
        Write a detailed SEO-friendly blog in Markdown titled:
        {state['blog']['title']}
        """
        response = self.llm.invoke(prompt)
        return {
            "blog": {
                "title": state["blog"]["title"],
                "content": response.content
            }
        }
