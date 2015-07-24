public class Subset{

public static void main(String[] args){
	int k = Integer.parseInt(args[0]);
	RandomizedQueue<String> queu=new RandomizedQueue<String>();
	while(!StdIn.isEmpty()){
		queu.enqueue(Stdin.readString());
	}
	if (queu.size()<k){
		k=queu.size();
	}
	while(k>0){
		System.out.println(queu.dequeue());
		k--;
	}
}
}