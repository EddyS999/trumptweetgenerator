import tweet 

def main():
    #receving data
    trump_tweets = []
    tweet.filtering(trump_tweets)
    tweet.write_in_txt(trump_tweets)
    G = tweet.load_graph("text.txt")

    #generate graph and sentence
    tweet.browsing_graph(G,20)
    reloaded_G = tweet.reload_graph("generated_sentence.txt")
    tweet.display(reloaded_G)

if __name__ == "__main__":
    main()
