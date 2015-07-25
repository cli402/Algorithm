import java.util.NoSuchElementException;
import java.util.Iterator;

public class RandomizedQueue<Item> implements Iterable<Item> {
   private Item[] queue=(Item[])new Object[1];
   private int size=0;
   public RandomizedQueue(){}                 // construct an empty randomized queue
   public boolean isEmpty(){return size()==0;}                 // is the queue empty?
   public int size(){return this.size;}                        // return the number of items on the queue
   public void enqueue(Item item){
      if(item== null){
         throw new NullPointerException("could not add null item");
      }
      this.size++;
      if (this.size()==this.queue.length){
         //double the size of the queue
         Item[] newqueue=(Item[])new Object[this.size()*2];
         for(int i=0;i<this.size();i++){
            newqueue[i]=this.queue[i];
         }
         this.queue=newqueue;}
         queue[size-1]=item;
         
      
   }           // add the item
   public Item dequeue(){
      if(isEmpty()){
         throw new NoSuchElementException("The queue is empty");
      }
      int rand = StdRandom.uniform(size);
      Item return_val=queue[rand];
      this.queue[rand]=this.queue[size-1];
      this.queue[size-1]=null;
      this.size--;

      //if the length of the queue
      if(this.size<=this.queue.length/4){
         Item[] newqueue=(Item[]) new Object[this.size];
         for (int i =0;i<this.size;i++){
            newqueue[i]=this.queue[i];
         }
         this.queue=newqueue;
      } 

      return return_val;
   }                    // remove and return a random item
   public Item sample(){
      if(this.size==0){
         throw new NoSuchElementException("The queue is empty");
      }
      int rand = StdRandom.uniform(size);
      return this.queue[rand];
   }                     // return (but do not remove) a random item
   
   private class Listiterator implements Iterator<Item>{
      private Item[] itequeu;
      private int size;
      public Listiterator(){
         itequeu=(Item[]) new Object[size()];
         for (int i=0;i<size();i++){
            itequeu[i]=queue[i];
         }

         //knuth shuffle
         for(int i =1;i<this.size;i++){
             int rand = StdRandom.uniform(i);
            Item temp=itequeu[i];
            itequeu[i]=itequeu[rand];
            itequeu[rand]=temp;
         }
         this.size=size();
      }
      @Override
      public boolean hasNext(){
         return this.size>0;
      }
      @Override
      public Item next(){
         if(!hasNext()){
            throw new NoSuchElementException("the queue is empty");
         }
         int rand = StdRandom.uniform(size);
         Item return_val=itequeu[rand];
         itequeu[rand]=itequeu[size-1];
         itequeu[size-1]=null;
         size--;
         return return_val;
      }
      @Override
      public void remove()
      {
         throw new UnsupportedOperationException("Could not use move in the iteration");
      }
      
   }
   public Iterator<Item> iterator(){
       return new Listiterator();
    }

   private void printqueue(){
    System.out.print("items are [ ");
     for (int i = 0; i < size; i++) {
       System.out.print((queue[i].toString()) + " ");
     }
     System.out.println("]");    
   }

            // return an independent iterator over items in random order
   public static void main(String[] args){
      RandomizedQueue test=new RandomizedQueue();
      for (int i =0;i<10;i++){
         test.enqueue(i);
      }
      System.out.println(test.size());
      test.printqueue();
      test.dequeue();
      test.dequeue();
      test.printqueue();
      Iterator test_iter=test.iterator();
      System.out.println(test_iter.next().toString());
      System.out.println(test_iter.next().toString());
   }   // unit testing
}