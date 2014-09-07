import java.util.*;

public class ScrabbleRunner{

    public static final char[][] BOARD = {
                       "octopus top".toCharArray(),
                       " a        2".toCharArray(),
                       " totaled  3".toCharArray(),
                       "       spit".toCharArray(),
                       "         l ".toCharArray(),
                       "         l ".toCharArray(),
                     };

    public static final int HEIGHT = BOARD.length;
    public static final int WIDTH = BOARD[0].length;

  public static void showBoard(){
    for(int r = 0; r < HEIGHT; r++){
      String rowline = "";
      for(int c = 0; c < WIDTH; c++){
        rowline += BOARD[r][c];
      }
      System.out.println(rowline);
    }
  }


  public static void showWords(List<String> words){
    for (String s : words){
      System.out.println(s);
    }
  }

  public static void showColumns(String[] columns){
    for (String s : columns){
      System.out.println(s);
    }
  }

  public static void addCharacter(int r, int c, List<String> words, String rowWord, String[] columns){
    rowWord += BOARD[r][c]; //add the character to the row word
    if (r == WIDTH-1 && rowWord.length() > 1) { //if this is the last char in row add word
       words.add(rowWord);
       rowWord = "";
    }
    if (columns[c] == null) { //if uninitialized initialize
       columns[c] = BOARD[r][c] + "";
    } else { //add the letter to the column
       columns[c] += BOARD[r][c];
    }
    if (c == HEIGHT-1 && columns[c].length() > 1) { //if this is the last character in the column add word
       words.add(columns[c]);
       columns[c] = "";
    }
  }


  public static void checkMutateStringInList(){
    List<String> myList = new ArrayList<String>();
    String myWord = "What up dawg!?";

    myList.add(myWord);
    System.out.println(myList.get(0));
    myWord = "";
    System.out.println(myList.get(0));
  }

  public static void addWord(String word ,List<String> words){
    if(word != null){
      if(word.length() > 1){ //add row word
        words.add(word);
      }
      word = null;
    }
  }

  public static void main(String[] args){
    showBoard();

    List<String> words = new ArrayList<String>();

    String[] columns = new String[WIDTH+1];
    for (int i = 0; i< columns.length; i++){
      columns[i] = "";
    }

    for(int r = 0; r < HEIGHT; r++){
      for(int c = 0; c < WIDTH; c++){
        if( BOARD[r][c] != ' '){ //if we have a character
          //addCharacter(r, c, words, rowWord, columns);
    columns[WIDTH] += BOARD[r][c]; //add the character to the row word
    //if (r == WIDTH-1 && rowWord.length() > 1) { //if this is the last char in row add word
    //   words.add(rowWord);
    //   rowWord = "";
    //}
    //if (columns[c] == null) { //if uninitialized initialize
    //   columns[c] = BOARD[r][c] + "";
    //} else { //add the letter to the column
    //   columns[c] += BOARD[r][c];
    //}
    //if (c == HEIGHT-1 && columns[c].length() > 1) { //if this is the last character in the column add word
    //   words.add(columns[c]);
    //   columns[c] = "";
    //}
        } else {
          addWord(columns[WIDTH], words);
          //addWord(columns[c], words);
        }
      }
      System.out.println(columns[WIDTH]);
    }
    showWords(words);
  }
}
