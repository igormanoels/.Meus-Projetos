package application;

import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.GridPane;

public class Tela {
	
	public Scene telaCalculadora() {
		
		GridPane grid = new GridPane();
		Scene principal = new Scene(grid);
		grid.getStylesheets().add(getClass().getResource("/style/application.css").toExternalForm());

        grid.setHgap(8);
        grid.setVgap(8);
		
		// Componentes da Tela
		Label txtDisplay = new Label("0");
		grid.add(txtDisplay, 0, 0);
		GridPane.setColumnSpan(txtDisplay, 4); // Ocupa 4 colunas
		
		
		Button btnMult = new Button("×");
		Button btnDiv = new Button("÷");
		Button btnAdc = new Button("+");
		Button btnSub = new Button("-");
		grid.add(btnMult, 0, 1);
		grid.add(btnDiv, 1, 1);
		grid.add(btnAdc, 2, 1);
		grid.add(btnSub, 3, 1);

		Button btnSete = new Button("7");
		Button btnOito = new Button("8");
		Button btnNove = new Button("9");
		Button btnPerc = new Button("%");
		grid.add(btnSete, 0, 2);
		grid.add(btnOito, 1, 2);
		grid.add(btnNove, 2, 2);
		grid.add(btnPerc, 3, 2);
		
		Button btnQuatro = new Button("4");
		Button btnCinco = new Button("5");
		Button btnSeis = new Button("6");
		Button btnRaiz = new Button("√");
		grid.add(btnQuatro, 0, 3);
		grid.add(btnCinco, 1, 3);
		grid.add(btnSeis, 2, 3);
		grid.add(btnRaiz, 3, 3);
		
		Button btnUm = new Button("1");
		Button btnDois = new Button("2");
		Button btnTres = new Button("3");
		Button btnIgual = new Button("=");
		grid.add(btnUm, 0, 4);
		grid.add(btnDois, 1, 4);
		grid.add(btnTres, 2, 4);
		grid.add(btnIgual, 3, 4);
		btnIgual.setId("botaoIgual");
		GridPane.setRowSpan(btnIgual, 2); // Ocupa duas linhas
				
		Button btnZero = new Button("0");
		Button btnPonto = new Button(".");
		Button btnVirgula = new Button(",");
		grid.add(btnZero, 0, 5);
		grid.add(btnPonto, 1, 5);
		grid.add(btnVirgula, 2, 5);
		
		
		GridPane.setMargin(txtDisplay, new Insets(16, 16, 8, 16));// Alteração das Margens: Top, Right, Bottom Left
		GridPane.setMargin(btnMult, new Insets(0, 0 , 0, 16)); 
		GridPane.setMargin(btnSete, new Insets(0, 0 , 0, 16)); 
		GridPane.setMargin(btnQuatro, new Insets(0, 0 , 0, 16)); 
		GridPane.setMargin(btnUm, new Insets(0, 0 , 0, 16)); 
		GridPane.setMargin(btnZero, new Insets(0, 0 , 0, 16)); 

		
		// Ações dos botões da aplicação
		principal.setOnKeyPressed((KeyEvent e) -> botoesFisicos(e));
		
		
		
//		if (e.getCode() == KeyCode.) {
//			System.out.println("Botão igual apertado.");
//		}

		
		/*
		 * btnIgual.setOnAction( e -> btnApertado() );
		 */		
		
		
		return principal;
		
	}
	
	//Método para mapear o teclado físico
	private void botoesFisicos(KeyEvent e) {
		if (e.isShiftDown()) {
			switch (e.getCode()) {
				case DIGIT8:
						System.out.println("Botão * apertado.");
					break;
				default:
					System.out.println(e.getCode().getName());
				break;
			}
			
		} else {
			switch (e.getCode()) {
				case EQUALS:
						System.out.println("Botão igual apertado.");
					break;
				case DIGIT0, NUMPAD0:
						System.out.println("0");
					break;
				case DIGIT1, NUMPAD1:
						System.out.println("1");
					break;
				case DIGIT2, NUMPAD2:
						System.out.println("2");
					break;
				case DIGIT3, NUMPAD3:
						System.out.println("3");
					break;
				case DIGIT4, NUMPAD4:
						System.out.println("4");
					break;
				case DIGIT5, NUMPAD5:
						System.out.println("5");
					break;
				case DIGIT6, NUMPAD6:
						System.out.println("6");
					break;
				case DIGIT7, NUMPAD7:
						System.out.println("7");
					break;
				case DIGIT8, NUMPAD8:
						System.out.println("8");
					break;
				case DIGIT9, NUMPAD9:
						System.out.println("9");
					break;
				case MINUS:
						System.out.println("-");
					break;
				case UNDEFINED:
						System.out.println("/");
					break;
				default:
						System.out.println(e.getCode().getName());
					break;
				}
		}
	}
	
	
	private void display(String valor) {
		StringBuffer resultado = new StringBuffer();
		
		resultado.append(valor);
		
	}
	
	
}
