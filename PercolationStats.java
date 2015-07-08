public class PercolationStats {
    private double[] number;
    private int T;
   public PercolationStats(int N, int T)     // perform T independent experiments on an N-by-N grid
   {
       
       if (N<=0 || T<=0){
       throw new IllegalArgumentException("Wrong Input!");}
       this.number=new double[T];
       for(int i=0;i<T;i++){
       this.number[i]=percolation(N);
       }
       this.T=T;
   }
   public double mean()                      // sample mean of percolation threshold
   {
       double sum=0.0;
       for(int i=0;i<this.T;i++){
       sum+=this.number[i];}
       return sum/this.T;
   }
   public double stddev()                    // sample standard deviation of percolation threshold
   {
       return StdStats.stddev(this.number);
   }
   public double confidenceLo()              // low  endpoint of 95% confidence interval
   {
       return (mean()-(1.96*stddev()/Math.sqrt(this.T)));
   }
   public double confidenceHi()              // high endpoint of 95% confidence interval
   {
       return (mean()+(1.96*stddev()/Math.sqrt(this.T)));
   }
   private double percolation(int N){
       Percolation per=new Percolation(N);
       int number_open=0;
       while(!per.percolates()){
       int i =StdRandom.uniform(1,N);
       int j=StdRandom.uniform(1,N);
       if(!per.isOpen(i,j)){
       per.open(i,j);
       number_open++;}
       }
       //System.out.println("The number_open is "+number_open);
       return (double)(number_open)/(double)(N*N);
   }
   public static void main(String[] args){
       int N=Integer.parseInt(args[0]);
       int T=Integer.parseInt(args[1]);
      
       PercolationStats stat=new PercolationStats(N,T);
       System.out.println("mean                    ="+stat.mean());
       System.out.println("stddev                  ="+stat.stddev());
       System.out.println("95% confidence interval ="+stat.confidenceLo()+","+stat.confidenceHi());
       
   }    // test client (described below)
}