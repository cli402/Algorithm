import java.util.LinkedList;
import java.util.List;

public class Board {
    private final int[][] block;
    private int move;

    public Board(int[][] blocks){
        this(blocks,0);
    } 
    private Board(int[][] blocks, int move){
        this.move= move;
        this.block=new int[blocks.length][blocks.length];
        for(int i = 0;i<blocks.length;i++){
            for (int j =0; j < blocks.length ; j++){
                this.block[i][j]=blocks[i][j];
            }
        }
    }          // construct a board from an N-by-N array of blocks
                                           // (where blocks[i][j] = block in row i, column j)
    public int dimension(){
        return this.block.length;
    }                 // board dimension N
    public int hamming(){
        int dist=0;
        for (int i = 0;i< block.length;i++){
            for (int j = 0 ; j< block.length; j++){
                if (block[i][j]!= valofboard(i,j) && block[i][j]!=0){
                    dist+=1;
                }
            }
        }
        dist+=this.move;
        return dist;
    }                   // number of blocks out of place
    public int manhattan() {
        int dist=0;
        for (int i =0 ;i < block.length;i++){
            for (int j = 0 ; j< block.length; j++){
                if(block[i][j] != i*block.length+j && block[i][j] !=0 ){
                    int value=block[i][j];
                    int row= (val-1)/this.dimension();
                    int col= (val-1)-row*this.dimension();
                    dist+=(Math.abs(row-i)+Math.abs(col-j));
                }
            }
        }
        return dist+this.move;
    }                // sum of Manhattan distances between blocks and goal
    public boolean isGoal(){
        for (int i =0 ;i < block.length;i++){
            for (int j = 0 ; j< block.length; j++){
                if(block[i][j] != this.valofboard(i,j){
                                return false; }}}
        return true;
    }                // is this board the goal board?
    public Board twin(){
        int[][] newblock= new int[this.dimension()][this.dimension()];
        for (int row = 0; row < dimension(); row++) {
            for (int col = 0; col < dimension(); col++) {
                newblock [row][col] = block[row][col];
            }
        }

        //Swap 2 blocks that are not 0
        int rowSwap = 0;
        if (newBlocks[0][0] == 0 || newBlocks[0][1] == 0) {
            rowSwap = 1;
        }
        
        int temp = newBlocks[rowSwap][0];
        newBlocks[rowSwap][0] = newBlocks[rowSwap][1];
        newBlocks[rowSwap][1] = temp;
        
        //Create new board to return
        return new Board(newBlocks, moves);
    }                    // a board that is obtained by exchanging two adjacent blocks in the same row
    public boolean equals(Object y){
        if (y == null) {
            return false;
        }
        
        if (this == y) {
            return true;
        }
        
        if (this.getClass() != y.getClass()) {
            return false;
        }
        
        Board that = (Board) y;
        
        if (this.dimension() != that.dimension()) {
            return false;
        }
        
        for (int row = 0; row < this.dimension(); row++) {
            for (int col = 0; col < this.dimension(); col++) {
                if (this.blocks[row][col] != that.blocks[row][col]) {
                    return false;
                }
            }
        }
        
        return true;
    }        // does this board equal y?
    public Iterable<Board> neighbors(){
        int spaceRowPos = 0;
        int spaceColPos = 0;
        
        //Find the empty square
        for (int row = 0; row < dimension(); row++) {
            for (int column = 0; column < dimension(); column++) {
                if (blocks[row][column] == 0) {
                    spaceRowPos = row;
                    spaceColPos = column;
                }
            }
        }
        
        List<Board> neighbors = new LinkedList<Board>();
        
        //Down
        if (spaceRowPos < dimension() - 1) {
            int[][] downBlocks = new int[dimension()][dimension()];
            for (int row = 0; row < dimension(); row++) {
                for (int col = 0; col < dimension(); col++) {
                    downBlocks[row][col] = blocks[row][col];
                }
            }
            
            int temp = downBlocks[spaceRowPos][spaceColPos];
            downBlocks[spaceRowPos][spaceColPos] = downBlocks[spaceRowPos + 1][spaceColPos];
            downBlocks[spaceRowPos + 1][spaceColPos] = temp;
            
            neighbors.add(new Board(downBlocks, moves + 1));
        }
        
        //Up
        if (spaceRowPos > 0) {
            int[][] upBlocks = new int[dimension()][dimension()];
            for (int row = 0; row < dimension(); row++) {
                for (int col = 0; col < dimension(); col++) {
                    upBlocks[row][col] = blocks[row][col];
                }
            }
            
            int temp = upBlocks[spaceRowPos][spaceColPos];
            upBlocks[spaceRowPos][spaceColPos] = upBlocks[spaceRowPos - 1][spaceColPos];
            upBlocks[spaceRowPos - 1][spaceColPos] = temp;
            
            neighbors.add(new Board(upBlocks, moves + 1));
        }
        
        //Left
        if (spaceColPos > 0) {
            int[][] leftBlocks = new int[dimension()][dimension()];
            for (int row = 0; row < dimension(); row++) {
                for (int col = 0; col < dimension(); col++) {
                    leftBlocks[row][col] = blocks[row][col];
                }
            }
            
            int temp = leftBlocks[spaceRowPos][spaceColPos];
            leftBlocks[spaceRowPos][spaceColPos] = leftBlocks[spaceRowPos][spaceColPos - 1];
            leftBlocks[spaceRowPos][spaceColPos - 1] = temp;
            
            neighbors.add(new Board(leftBlocks, moves + 1));
        }
        
        //Right
        if (spaceColPos < dimension() - 1) {
            int[][] rightBlocks = new int[dimension()][dimension()];
            for (int row = 0; row < dimension(); row++) {
                for (int col = 0; col < dimension(); col++) {
                    rightBlocks[row][col] = blocks[row][col];
                }
            }
            
            int temp = rightBlocks[spaceRowPos][spaceColPos];
            rightBlocks[spaceRowPos][spaceColPos] = rightBlocks[spaceRowPos][spaceColPos + 1];
            rightBlocks[spaceRowPos][spaceColPos + 1] = temp;
            
            neighbors.add(new Board(rightBlocks, moves + 1));
        }
        
        return neighbors;
    }     // all neighboring boards
    public String toString()               // string representation of this board (in the output format specified below)
    private int valofboard(int i,int j){
        if(i == this.dimension()-1 && j == this.dimension()-1）{
            return 0;
        }
        else{
            return i*this.dimension+j+1;
        }
    }
    public static void main(String[] args) // unit tests (not graded)
}