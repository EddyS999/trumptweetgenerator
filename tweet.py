import csv
import matplotlib.pyplot as plt
import random
import networkx as nx



#filtering csv file and passing informations through a list 
def filtering(trump_tweets) -> None:
    file = open("realdonaldtrump.csv", encoding="utf8")
    contenu = csv.reader(file)
    for element in contenu:
        for word in element[2].split(" "):
            if not word.__contains__("/") and not word.__contains__(")") and not word.__contains__("\\") and not word.__contains__("'"):
                trump_tweets.append(word.replace("!","").replace(".","").replace("http","").replace("https","").replace("s:","")
                    .replace("//","").replace(":","").replace("www","").replace("@","").replace("(","").replace("\"","").replace("*","")
                             .replace("“",""))
        trump_tweets.append("##")
    file.close()


#wrinting trump tweets in a file with the previous list 
def write_in_txt(trump_tweets, nodes=10) -> None:
    output = ""
    for i, item in enumerate(trump_tweets):
        if item == "##":
            output += "\n"
        else:
            output += item
            if i < len(trump_tweets) - 1 and trump_tweets[i + 1] != "##":
                output += ";"
        
        if i >= nodes: 
            with open("text.txt","w", encoding="UTF-8") as f:
                 f.write(output)
            return 
    
    

def load_graph(source):
    G = nx.Graph()
    file = open(source, encoding='UTF-8')
    file.readline()
    content = file.read()
    file.close()
    line_list = content.split("\n")

    for line in line_list:
        couple = line.split(";")
        for i in range(len(couple) - 1):
            G.add_edge(couple[i], couple[i + 1])
            if couple[i] not in G:
                G.add_node(couple[i],nom=couple[i])
    return G


def generate_random_color(G):
    color_map = []
    for node in G:
        if random.randint(0, 1) == 0:
            color_map.append('blue')
        else:
            color_map.append('green')
    return color_map


def generate_random_edge_color(G):
    color_map = []
    for node in G.edges():
        if random.randint(0, 1) == 0:
            color_map.append('red')
        else:
            color_map.append('orange')
    return color_map


def set_node_size(G):
    d = dict(nx.degree(G))
    node_s = [v * 10 for v in d.values()]
    return node_s


def display(G):
    node_color = generate_random_color(G)
    edge_color = generate_random_edge_color(G)
    node_size = set_node_size(G)

    nx.draw(G, node_color=node_color, edge_color=edge_color, node_size=node_size, with_labels=True)
    plt.show()

def main(): 
    trump_tweets = []
    nodes = int(input("how many nodes to generate ?"))
    filtering(trump_tweets)
    write_in_txt(trump_tweets,nodes)
    G = load_graph("text.txt")
    display(G)

if __name__ == "__main__": 
    main()

#G = load_graph("text.txt")
#display(G)