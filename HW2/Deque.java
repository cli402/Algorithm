import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
 private int size=0;
 private Node first=null;
 private Node last=null;
 private class Node{
  Item item;
  Node next;
  Node previous;
 }

   private class ItemIterator implements Iterator<Item> {

     private Node next = null;
  
      private ItemIterator() {
       next = first;
  }
  
  @Override
  public boolean hasNext() {
   return (next != null);
  }

  @Override
  public Item next() {
   if (!hasNext()) {
    throw new NoSuchElementException();
   }
   Item item = next.item;
   next = next.next;
   return item;
  }
  
  @Override
  public void remove() {
   throw new UnsupportedOperationException(); 
  }
   }
   public Deque(){}                           // construct an empty deque
   public boolean isEmpty()
   {return this.size==0;}                 // is the deque empty?
   public int size(){return this.size;}                        // return the number of items on the deque
   public void addFirst(Item item){
    if(item==null){
     throw new NullPointerException("could not add null item!");
    }
    else{
     Node add=new Node();
     add.item=item;
     this.size++;
     if(size==1){
      this.first=add;
      this.last=add;
     }
     else{
      this.first.previous=add;
      add.next=first;
      first=first.previous;
     }
    }   }       // add the item to the front
   public void addLast(Item item){
    if(item == null){
     throw new NullPointerException("Could not add null item");
    }
    else{
     Node add=new Node();
     add.item=item;
     this.size++;
    
     if(size==1){
      this.first=add;
      this.last=add;
     }
     else{
      last.next=add;
      add.previous=last;
      last=last.next;
     }
    }}           // add the item to the end
   public Item removeFirst(){
    if(this.isEmpty()){
     throw new NoSuchElementException("The queue is empty"); 
    }
    else{
     Item item=this.first.item;
     this.first=this.first.next;
     this.size--;
      this.first.previous=null;
     if (size()==0){
      this.last=null;
     }
     else{
     }
    return item;
    }

   }                // remove and return the item from the front
   public Item removeLast(){
    if(this.isEmpty()){
     throw new NoSuchElementException("The queue is empty");
    }
    else{
     Item item=this.last.item;
     this.last=this.last.previous;
     this.last.next=null;
     this.size--;
     if(size()==0){
      this.first=null;
     }
     return item;
    }
   }                 // remove and return the item from the end
   @Override
   public Iterator<Item> iterator(){
      return new ItemIterator();
   }  

   private void printqueue(){
      System.out.println("Queue:[");
      Iterator test=this.iterator();
      while(test.hasNext()){
      System.out.println(test.next().toString()+" ");
      }
      System.out.println(" ]");
   }
          // return an iterator over items in order from front to end
   public static void main(String[] args)   // unit testing
   {
       Deque test=new Deque();
      for (int i =0;i<10;i++){
         test.addFirst(i);
      }
      System.out.println(test.size());
      test.printqueue();
      test.removeLast();
      test.removeLast();
      test.printqueue();
      Iterator test_iter=test.iterator();
      System.out.println(test_iter.next().toString());
      System.out.println(test_iter.next().toString());

}
}

