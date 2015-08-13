import java.util.Comparator;
public class Solver {
	private class Node{
		Borad board;
		Node parent;
		public Node(Board board, Node parent){
			this.board=board;
			this.parent=parent;
		}
	}

	private MinPQ<Node> queue;
	private MinPQ<Node> swapQueue;
	private boolean queue_sovable;
	private boolean swap_queue_sovable;
	private Node endNode;

    public Solver(Board initial) throws NullPointerException{
    	if (initial == null){
    		throw new NullPointerException("The parameter is null !");
    	}
    	this.queue=new MinPQ<Node>(boardComparator);
    	this.swapQueue= new MinPQ<Node>(boardComparator);
    	this.queue_sovable=false;
    	this.swap_queue_sovable=false;
    	this.endNode=null;

    	Node node=new Node(initial,null);
    	queue.insert(node);

    	Node swapnode = new Node(initial.twin(),null);
    	swapQueue.insert(swapnode);

    	while (!queue_sovable && !swapQueue){
    		queue_sovable=solve_board(queue);
    		swap_queue_sovable=solve_board(swapQueue);
    	}
    } 

    private boolean solve_board(MinPQ<Node> que){
    	Node current=que.delMin();
    	if (current.board.isGoal()){
    		this.endNode=current;
    		return true;
    	}
    	for(Board b : current.board.neighbors()){
    		if(current.parent == null  || !b.equals(current.parent.board)){
    			Node neighbor = new Node(b,current);
    			que.insert(neighbor);
    		}
    	}
    	return false;
    }
              // find a solution to the initial board (using the A* algorithm)
    public boolean isSolvable(){
    	return queue_sovable;
    }            // is the initial board solvable?
    public int moves() {
    	if (isSolvable()) {
    		Node current = endNode;
    		int moves = 0;
    		
    		while(current.parent != null) {
    			moves++;
    			current = current.parent;
    		}
    		
    		return moves;
    	} else {
    		return -1;
    	}
    }                    // min number of moves to solve initial board; -1 if unsolvable
    public Iterable<Board> solution() {
    	if (isSolvable()) {
    		//create new list and return it
    		Stack<Board> sol = new Stack<Board>();
    		
    		Node current = endNode;
    		sol.push(endNode.board);
    		
    		while(current.parent != null) {
    			sol.push(current.parent.board);
    			current = current.parent;
    		}
    		
    		return sol;
    	} else {
    		return null;
    	}
    }

    private static Comparator<Node> boardComparator = new Comparator<Node>() {

		@Override
		public int compare(Node o1, Node o2) {
			return o1.board.manhattan() - o2.board.manhattan();
		}
    };

         // sequence of boards in a shortest solution; null if unsolvable
    public static void main(String[] args) // solve a slider puzzle (given below)
}