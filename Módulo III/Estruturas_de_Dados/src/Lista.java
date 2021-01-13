import java.util.ArrayList;

public class Lista {

	public static void main(String[] args) {
		ArrayList<String> carros = new ArrayList<String>();

		carros.add("Uno");
		carros.add("Gol");
		carros.add("Palio");

		carros.add(1, "Sandero"); // Adiciona o Sandero na posi��o 1, empurrando quem ta no 1 para posi��o 2.

		// ----------------------------------------------------
		System.out.println("Verificando a exist�ncia de um elemento: ");
		if (carros.contains("Gol")) { // Verifica se a lista cont�m o elemento solicitado, retornando TRUE ou FALSE
			System.out.println("Existe o elemento Gol no array!");
		} else {
			System.out.println("N�o existe o elemento Gol no array!");
		}

		// ----------------------------------------------------
		carros.add("Gol");
		System.out.println("");
		System.out.println("Identificando o indice da primeira ocorrencia de um elemento: ");
		int primeiraPosicaoGol = carros.indexOf("Gol"); // Retorna o indice da PRIMEIRA ocorrencia, caso o elemento n�o
														// exista ele retorna -1
		System.out.println(primeiraPosicaoGol);

		// ----------------------------------------------------
		System.out.println("");
		System.out.println("Identificando o indice da �ltima ocorrencia de um elemento: ");
		int ultimaPosicaoGol = carros.lastIndexOf("Gol");
		System.out.println(ultimaPosicaoGol);

		// ----------------------------------------------------
		System.out.println("");
		System.out.println("Adicionando: ");
		for (int i = 0; i < carros.size(); i++) {
			System.out.println(carros.get(i));
		}

		// ----------------------------------------------------
		carros.set(0, "Novo Uno"); // Altera o elemento daquele indice
		System.out.println("");
		System.out.println("Alterando o elemento do indice informado: ");
		for (int i = 0; i < carros.size(); i++) {
			System.out.println(carros.get(i));
		}

		// ----------------------------------------------------
		carros.remove(0);
		carros.remove(1);

		System.out.println("");
		System.out.println("Ap�s remo��o: ");
		for (int i = 0; i < carros.size(); i++) {
			System.out.println(carros.get(i));
		}

		// ----------------------------------------------------
		carros.clear();
		System.out.println("");
		System.out.println("Limpando a lista:");
		System.out.println(carros);

	}

}
