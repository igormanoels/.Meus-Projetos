package application;

import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class Tela {
	
	public Scene telaCalculadora(Stage tela) {
		
		GridPane grid = new GridPane();
		Scene principal = new Scene(grid, 320, 514);
		
		
		// Componentes da Tela
		TextField txtDisplay = new TextField();
		grid.add(txtDisplay, 0, 0);
		GridPane.setColumnSpan(txtDisplay, 4);
		
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
		GridPane.setRowSpan(btnIgual, 2);
		
		Button btnZero = new Button("0");
		Button btnPonto = new Button(".");
		Button btnVirgula = new Button(",");
		grid.add(btnZero, 0, 5);
		grid.add(btnPonto, 1, 5);
		grid.add(btnVirgula, 2, 5);
		
		return principal;
		
	}
}
