public class Percolation {
   private boolean[] array;
   private int number;
   private WeightedQuickUnionUF wquuf;
   
   // create N-by-N grid, with all sites blocked
   public Percolation(int N){
       if(N<=0){
       throw new java.lang.IndexOutOfBoundsException ();}
       array=new boolean[N*N];
       for(int i =0;i<N;i++){
           for(int j =0;j<N;j++){
           array[i*N+j]=false;}
   }
       this.number=N;
       this.wquuf=new WeightedQuickUnionUF(N*N);
       
   }
   // open site (row i, column j) if it is not open already
   public void open(int i, int j){
       if(i<1 || i > this.number || j<1 || j> this.number)
       {throw new java.lang.IndexOutOfBoundsException ();}
       i=i-1;
       j=j-1;
       array[i*this.number+j]=true;
       int index=i*this.number+j;
       //check if the above is open
       if (i==0){
       wquuf.union(0,index);
       }
       else{
           if(array[index-this.number]){
           wquuf.union(index,index-this.number);}
           }
     //check if the below is open
       if (i==this.number-1){
       wquuf.union(index,this.number^2-1);}
       else{
           if(array[index+this.number]){
           wquuf.union(index,this.number+index);}
           }
     //check if the right neighbour is open
       if(j!=0){
           if(array[index-1]){
           wquuf.union(index,index-1);
           }
       }
       //check if the left neighbour is open
       if(j!=this.number-1){
           if (array[index+1]){
           wquuf.union(index,index+1);
           }}

}

   // is site (row i, column j) open?
   public boolean isOpen(int i, int j){
       if(i<1 || i > this.number || j<1 || j> this.number)
       {throw new java.lang.IndexOutOfBoundsException ();}
       return array[(i-1)*this.number+(j-1)];
   }
   
   // is site (row i, column j) full?
   public boolean isFull(int i, int j){
       int index=(i-1)*this.number+(j-1);
       return wquuf.connected(0,index);
   }  
   // does the system percolate?
   public boolean percolates(){             
       return wquuf.connected(0,this.number^2-1);
   }
}