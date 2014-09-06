expedia.com

             e
      p               x
   e     d         i      a
 c   .            m  o

[[lobster to],
[ r        ]
[ b        ]
[          ]
[ i        ]
[ next     ]]


int height = brd.length
int width = brd[0].length

words = []
columns = [width]
for(int r = 0; r < height; r++){
 row_wrd = ""
 for(int c = 0; c < width; c++){
   if( brd[r][c] != ' '){
     row_wrd += brd[r][c];
     if (r == width-1 && row_wrd.length > 1) {
        words.append(row_wrd);
        row_wrd = "";
    }
     if (c == height-1 && columns[c].length > 1) {
        words.append(columns[c]);
        columns[c] = "";
    }
     if (columns[c] == null) {
        columns[c] = brd[r][c]
     } else {
        columns[c] += brd[r][c]
     }
   } else {
     if(row_wrd.length > 1){
        words.append(row_wrd);
        row_wrd = "";
    }
    if(columns[c].length > 1 {
        words.append(columns[c]);
        columns[c] = "";
    }

   }
   
   
 }

}

def gen_cols(brd):
    for 

cols = gen_cols(brd);

for row in brd:
    row_wrds = "".join(row).split(' ')
for col in cols:
    col_wrds = "".join(col).split(' ')



