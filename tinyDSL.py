class TAG:
    
    def __init__(self, type, content, attributes = None, closing = True, doctype = False): # constructor takes 5 parameters: type, content, attributes, closing and doctype
        self.type = type
        self.content = content
        self.attributes = attributes
        self.sub_tags = []
        self.closing = closing
        self.doctype = doctype
        
    def to_string(self, prettify=False): # method that returns the string representation of the tag
        endStr = ""
        
        if prettify: # add a line break if prettify is True
            endStr = "\n"
        
        other_tag_str = ""
        for tag in self.sub_tags:
            other_tag_str += tag.to_string(prettify=prettify) # add the string representation of the child tags to the other_tag_str
            
        if other_tag_str:
            return f"<{self.type}>{other_tag_str}</{self.type}>" + endStr # return the string representation of the tag with the child tags
        
        if self.attributes: # add the attributes to the tag if they exist
            attributes = ""
            for key, value in self.attributes.items():
                attributes += f" {key}='{value}'"
            
            if self.closing:
                return f"<{self.type}{attributes}>{self.content}</{self.type}>" + endStr # return the string representation of the tag with the content
            else:
                return f"<{self.type}{attributes}/>" + endStr # return the string representation of the tag with the attributes
            
        if self.doctype: # return the string representation of the doctype
            return f"<{self.type}{attributes}/>" + endStr 
        
        return f"<{self.type}>{self.content}</{self.type}>" + endStr
    
    
    def add(self, tags, tab_index = 0): # method that adds child tags to the tag
        tabChar = "\t"
        tab_index += 1
        if tab_index > 0:
            for i in range(tab_index):
                #create a tab indent before adding the child tags
                self.sub_tags.append(tabChar * i)
        self.sub_tags = tags
        print(self.sub_tags)
        return self
    
class A(TAG): # Link tag
    
    def __init__(self, content, attributes=None):
        super().__init__("a", content, attributes)


class HTML(TAG): # HTML tag
    
    def __init__(self, content, attributes=None):
        super().__init__("html", content, attributes)


class H1(TAG): # H1 tag
    
    def __init__(self, content, attributes=None):
        super().__init__("h1", content, attributes)

class H2(TAG): # H2 tag
    
    def __init__(self, content, attributes=None):
        super().__init__("h2", content, attributes)

class Body(TAG): # Body tag
    
    def __init__(self, content, attributes=None):
        super().__init__("body", content, attributes)
        
class Head(TAG): # Head tag
    
    def __init__(self, content, attributes=None):
        super().__init__("head", content, attributes)

class Meta(TAG): # Meta tag
    
    def __init__(self, content, attributes=None, closing=False):
        super().__init__("meta", content, attributes, closing)

class Title(TAG): # Title tag
    
    def __init__(self, content, attributes=None):
        super().__init__("title", content, attributes)

class Link(TAG): # Link tag
    
    def __init__(self, content, attributes=None, closing=False):
        super().__init__("link", content, attributes, closing)

class Script(TAG): # Script tag
    
    def __init__(self, content, attributes=None):
        super().__init__("script", content, attributes)
        
class HTMLDOCTYPE(TAG): # HTML DOCTYPE tag
    
    def __init__(self, content, attributes=None):
        super().__init__("!DOCTYPE html", content, attributes)


