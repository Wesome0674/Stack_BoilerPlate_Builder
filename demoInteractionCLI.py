from tinyDSL import *

class Questionner:
    
    def __init__(self):
        self.authorized_tags = ["html", "head", "body", "h1", "h2", "a"] # list of authorized tags
        self.authorized_styles = ["light", "dark"] # list of authorized styles
        self.html = HTML("") # create an HTML object
        self.body = Body("", {"lang":"fr"}) # create a Body object
        self.tags = [] # list of tags
        self.args = {} # dictionary of arguments
        
    def askProjectName(self):
        projectName = input("Quel est le nom du projet?") # ask the project name
        return projectName
    
    def askProjectType(self):
        projectType = input("Quel est le type du projet? (web/next)") # ask the project type
        return projectType

    def askProjectStyle(self):
        projectStyle = input("Quel est le style du projet? (light/dark)") # ask the project style
        if projectStyle not in self.authorized_styles:
            print("Style non autorisé")
            return self.askProjectStyle()
        else:
            return projectStyle
        
    def askTag(self):
        newTag = input("Quel tag voulez vous ajouter? (h1/h2/a...)") # ask the tag
        if newTag not in self.authorized_tags:
            print("Tag non autorisé")
            return self.askTag()
        else:
            content = self.askContent(newTag) # ask the content for the tag
            self.askArguments(newTag) # ask the arguments for the tag
            if newTag == "h1":
                self.tags.append(H1(content, self.args)) # add the tag to the list of tags
               
            if newTag == "h2":
                self.tags.append(H2(content, self.args))
                
            res = input("Voulez vous ajouter un autre tag? (y/n)") # ask if the user wants to add another tag
            if res == "y":
                return self.askTag()
            else:
                final_tags = [*self.tags] 
                final_tags.append(A("Check out my portfolio", {"href":"https://cbk-portfolio.com"}))
                final_tags.append(Script("", {"src":"script.js"}))
                self.body.add(final_tags)
        
    def askContent(self, tag):
        content = input("Quel contenu pour le tag?") # ask the content for the tag
        return content
        
    def askArguments(self, tag):
        arguments = input("Quels sont les arguments du tag?") # ask the arguments for the tag
        argsContent = input("Quel contenu pour l'argument?") # ask the content for the argument
        self.args[arguments] = argsContent # add the argument to the dictionary of arguments
        resArgs = input("Voulez vous ajouter un autre argument? (y/n)") # ask if the user wants to add another argument
        if resArgs == "y":
            return self.askArguments(tag) # ask the arguments for the tag
        else:
            return self.args # return the dictionary of arguments
        
    def buildHTML(self): # build the HTML object
        page = ""
        doctype = HTMLDOCTYPE("")
        page += doctype.to_string(prettify=True)
        # Add head and body to HTML tag
        self.html.add([
            Head("").add([
                Meta("", {"charset":"UTF-8"}),
                Meta("", {"name":"viewport", "content":"width=device-width, initial-scale=1.0"}),
                Link("", {"rel":"stylesheet", "href":f"styles/{style}.css"}),
                Link("", {"rel":"stylesheet", "href":"styles/reset.css"}),
                Title(name)
            ]),
            self.body
        ])
        page += self.html.to_string(prettify=True)
        # Return DOCTYPE followed by HTML
        return page
    
    def buildCSS(self): # build the CSS object
        theme = ""
        
        # Load the theme based on the selected style
        if style == "light":
            theme += open("templates/light_theme.txt", "r").read()
        else:
            theme += open("templates/dark_theme.txt", "r").read()
        
        for tag in self.tags:
            if tag.attributes:
                for arg, value in tag.attributes.items():
                    if arg == "class":
                        theme += f".{value} {{\n  /* add styles here */\n}}\n"
                    elif arg == "id":
                        theme += f"#{value} {{\n  /* add styles here */\n}}\n"
                    else:
                        pass
        return theme

    def buildResetCSS(self): # build the reset CSS object
        return open("templates/reset_css.txt", "r").read()
    
    def buildJS(self): # build the JS object
        return open("templates/script_js.txt", "r").read()


questionner = Questionner() # create a Questionner object

type = questionner.askProjectType() # ask the project type
name = questionner.askProjectName() # ask the project name

if type == "web":
    style = questionner.askProjectStyle() # ask the project style
    questionner.askTag() # ask the tags
elif type == "next":
     pass
else:
    print("Type de projet non valide")
    exit()

