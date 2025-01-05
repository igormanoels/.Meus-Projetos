package application;
	
import javafx.application.Application;
import javafx.stage.Stage;


public class Main extends Application {
	
	@Override
	public void start(Stage stage) {
		try {
			Tela tela = new Tela();
			stage.setScene(tela.telaCalculadora());
			//stage.setResizable(false); // Bloqueia o redimensionamento da tela
			//stage.initStyle(StageStyle.UNDECORATED); // Também é possivel remove a barra do windows
			
			stage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
