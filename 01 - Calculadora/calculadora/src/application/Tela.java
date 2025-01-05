package application;

import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.GridPane;

public class Tela {
	
	private Label txtDisplay = new Label();
	private StringBuffer expressao = new StringBuffer();
	private Operacoes op = new Operacoes();
	
	public Scene telaCalculadora() {
		
		GridPane grid = new GridPane();
		Scene principal = new Scene(grid);
		grid.getStylesheets().add(getClass().getResource("/style/application.css").toExternalForm());

        grid.setHgap(8);
        grid.setVgap(8);
		
		// Componentes da Tela
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
		Button btnRaiz = new Button("√");
		grid.add(btnSete, 0, 2);
		grid.add(btnOito, 1, 2);
		grid.add(btnNove, 2, 2);
		grid.add(btnRaiz, 3, 2);
		
		Button btnQuatro = new Button("4");
		Button btnCinco = new Button("5");
		Button btnSeis = new Button("6");
		Button btnClear = new Button("CE");
		grid.add(btnQuatro, 0, 3);
		grid.add(btnCinco, 1, 3);
		grid.add(btnSeis, 2, 3);
		grid.add(btnClear, 3, 3);
		
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
		

		btnMult.setOnAction(e -> display("*"));
		btnDiv.setOnAction(e -> display("÷"));
		btnAdc.setOnAction(e -> display("+"));
		btnSub.setOnAction(e -> display("-"));
		
		btnSete.setOnAction(e -> display("7"));
		btnOito.setOnAction(e -> display("8"));
		btnNove.setOnAction(e -> display("9"));
		btnRaiz.setOnAction(e -> display("√"));
		
		btnQuatro.setOnAction(e -> display("4"));
		btnCinco.setOnAction(e -> display("5"));
		btnSeis.setOnAction(e -> display("6"));
		
		btnUm.setOnAction(e -> display("1"));
		btnDois.setOnAction(e -> display("2"));
		btnTres.setOnAction(e -> display("3"));

		btnZero.setOnAction( e -> display("0"));
		btnPonto.setOnAction(e -> display("."));
		btnVirgula.setOnAction(e -> display(","));
		
		btnClear.setOnAction(e -> limparDisplay());
		
		btnIgual.setOnAction(e -> calcularExpressa()); 
		
		limparDisplay();

		return principal;
		
	}
	
	//Método para mapear o teclado físico
	private void botoesFisicos(KeyEvent e) {
		if (e.isShiftDown()) {
			switch (e.getCode()) {
				case DIGIT8:
					display("*");
					break;
				default:
					System.out.println(e.getCode().getName());
				break;
			}
			
		} else {
			switch (e.getCode()) {
				case EQUALS:
						calcularExpressa();
					break;
				case DIGIT0, NUMPAD0:
						display("0");
					break;
				case DIGIT1, NUMPAD1:
						display("1");
					break;
				case DIGIT2, NUMPAD2:
						display("2");
					break;
				case DIGIT3, NUMPAD3:
						display("3");
					break;
				case DIGIT4, NUMPAD4:
						display("4");
					break;
				case DIGIT5, NUMPAD5:
						display("5");
					break;
				case DIGIT6, NUMPAD6:
						display("6");
					break;
				case DIGIT7, NUMPAD7:
						display("7");
					break;
				case DIGIT8, NUMPAD8:
						display("8");
					break;
				case DIGIT9, NUMPAD9:
						display("9");
					break;
				case MINUS:
						display("-");
					break;
				case UNDEFINED:
						display("÷");
					break;
				case PERIOD:
						display(".");
					break;
				case COMMA:
						display(",");
					break;
				case DELETE:
						limparDisplay();
					break;
				default:
						System.out.println(e.getCode().getName());
					break;
				}
		}
	}
	
	
	private void display(String valor) {
		expressao.append(valor);
		System.out.println(expressao);
		txtDisplay.setText(String.valueOf(expressao));
	}

	
	private void limparDisplay() {
		expressao.delete(0, expressao.length());
		txtDisplay.setText("0");
	}
	
	
	private void calcularExpressa() {
		txtDisplay.setText(op.realizarCalculo(expressao));
	}
}
