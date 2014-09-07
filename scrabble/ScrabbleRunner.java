import java.util.*;

public class ScrabbleRunner{

  public static void showBoard(char[][] board){
    int height = board.length;
    int width = board[0].length;
    for(int r = 0; r < height; r++){
      String rowline = "";
      for(int c = 0; c < width; c++){
        rowline += board[r][c];
      }
      System.out.println(rowline);
    }

  }

  public static void main(String[] args){
    List<String> words = new ArrayList<String>();

    char[][] board = { "octopus top".toCharArray(),
                       " a        2".toCharArray(),
                       " totaled  3".toCharArray(),
                       "       spit".toCharArray(),
                       "         l ".toCharArray(),
                       "         l ".toCharArray(),
                     };
    int height = board.length;
    int width = board[0].length;

    String[] columns = new String[width];
    for(int r = 0; r < height; r++){
      String row_wrd = "";
      for(int c = 0; c < width; c++){
        if( board[r][c] != ' '){
          row_wrd += board[r][c];
          if (r == width-1 && row_wrd.length() > 1) {
             words.append(row_wrd);
             row_wrd = "";
          }
          if (c == height-1 && columns[c].length() > 1) {
             words.append(columns[c]);
             columns[c] = "";
          }
          if (columns[c] == null) {
             columns[c] = board[r][c] + "";
          } else {
             columns[c] += board[r][c];
          }
        } else {
          if(row_wrd.length() > 1){
             words.append(row_wrd);
             row_wrd = "";
          }
          if(columns[c].length() > 1 ){
              words.append(columns[c]);
              columns[c] = "";
          }
        }
      }
    }
  }
}
