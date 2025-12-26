# src/graphs/graph_builder.py
from langgraph.graph import StateGraph, START, END
from src.nodes.blog_node import BlogNode
from src.states.blogstate import BlogState

class GraphBuilder:
    def __init__(self, llm):
        self.graph = StateGraph(BlogState)
        self.llm = llm

    def build_topic_graph(self):
        node = BlogNode(self.llm)

        self.graph.add_node("title_creation", node.title_creation)
        self.graph.add_node("content_generation", node.content_generation)

        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph.compile()

    def setup_graph(self,usecase):
        """
        Setup the graph
        """
        if usecase=="topic":
            self.graph=self.build_topic_graph()
        else:
            raise ValueError("Invalid usecase")

        return self.graph.compile()    
        
