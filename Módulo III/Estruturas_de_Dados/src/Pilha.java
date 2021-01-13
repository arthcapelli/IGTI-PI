import java.util.Stack;

public class Pilha {

	public static void main(String[] args) {
		Stack<String> stack = new Stack<>();
		Stack<String> stackVazia = new Stack<>();
		
		//adicionando elementos
		stack.add("Livro 1");
		stack.add("Livro 2");
		stack.add("Livro 3");
		stack.add("Livro 4");
		stack.add("Livro 5");
		
		System.out.println(stack);
		
		
		//removendo o último elemento da pilha
		System.out.println("Elemento removido: " +  stack.pop());
		
		System.out.println(stack);
		
		//verifica o último elemento da pilha
		System.out.println("Elemento verificado: " + stack.peek());
		System.out.println(stack);
		
		//procurar elemento na pilha e retorna o indice do mesmo
		System.out.println(stack.search("Livro 3"));
		
		//verifica se a pilha está vazia (TRUE ou FALSE)
		System.out.println(stack.isEmpty());
		System.out.println(stackVazia.isEmpty());

	}

}
