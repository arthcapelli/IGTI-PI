package sequencia;

import java.util.Scanner;
import java.util.Stack;

public class Sequencia {
	private Scanner scanner = new Scanner(System.in);

	private String mostrarMenu() {
		System.out.println("Digite a sequencia para verifica��o ou digite sair para encerrar:");

		return scanner.nextLine();
	}

	public void iniciar() {
		// Sequencias v�lidas () - [] - (()) - [[]] - [()] - ([])
		// Sequencias inv�lidas (( - )) - [[ - ]] - ([))

		String sequencia = mostrarMenu();
		while (!sequencia.equals("sair")) {
			Stack<String> stack = new Stack<>();
			boolean isSequenciaOk = true;

			for (int i = 0; i < sequencia.length(); i++) {
				if (!isSequenciaOk) {
					break;
				}
				char c = sequencia.charAt(i);

				switch (c) {
				case ')':
					if (stack.isEmpty()) {
						System.out.println("Sequencia inv�lida!");
						sequencia = mostrarMenu();
						isSequenciaOk = false;

					} else {
						String elemento = stack.pop();
						if (!elemento.equals("(")) {
							System.out.println("Sequencia inv�lida!");
							sequencia = mostrarMenu();
							isSequenciaOk = false;
						}
					}
					break;

				case ']':
					if (stack.isEmpty()) {
						System.out.println("Sequencia inv�lida!");
						sequencia = mostrarMenu();
						isSequenciaOk = false;

					} else {
						String elemento = stack.pop();
						if (!elemento.equals("[")) {
							System.out.println("Sequencia inv�lida!");
							sequencia = mostrarMenu();
							isSequenciaOk = false;
						}
					}
					break;

				default:
					stack.push(String.valueOf(c));

				}

			}
			if (!sequencia.equals("sair")) {
				if (stack.isEmpty()) {
					System.out.println("Sequencia correta!");
				} else {
					System.out.println("Sequencia inv�lida!");
				}
				sequencia = mostrarMenu();
			}
		}
	}
}
