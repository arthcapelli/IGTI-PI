import java.util.LinkedList;
import java.util.Queue;

public class Fila {

	public static void main(String[] args) {
		Queue<String> fila = new LinkedList<>();

		// adicionando elementos
		fila.add("Pessoa 1");
		fila.add("Pessoa 2");
		fila.add("Pessoa 3");
		fila.add("Pessoa 4");
		fila.add("Pessoa 5");

		System.out.println(fila);

		// removendo elementos, o primeiro a sair será o primeiro a ter entrado
		System.out.println("Elemento removido: " + fila.remove());
		System.out.println(fila);

		// verificando o primeiro elemento da fila
		System.out.println("Primeiro da fila: " + fila.peek());
		System.out.println(fila);

		// procurar elemento na fila (TRUE ou FALSE)
		System.out.println(fila.contains("Pessoa 3"));

		// verificar tamanho da fila
		System.out.println("Tamanho: " + fila.size());

		// verificar se está vazio ou não (TRUE ou FALSE)
		System.out.println(fila.isEmpty());

		// remove todos elementos
		// fila.clear();

	}

}
