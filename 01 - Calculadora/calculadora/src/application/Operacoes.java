package application;

import java.util.ArrayList;
import java.util.List;

public class Operacoes {
	
	public List<String> numeros;
	public List<String> operadores;
	
	public Operacoes() {
		this.numeros = new ArrayList<>();
		this.operadores = new ArrayList<>();
	}
	
	
	public String realizarCalculo(StringBuffer expressao) {
		String operador = "";
		double a = 1, b = 0;
		
		System.out.println(expressao);
		
		switch (operador) {
		case "*":
			multiplicar(a, b);
			break;
		case "÷":
			dividir(a, b);
			break;
		case "+":
			somar(a, b);
			break;
		case "-":
			subtrair(a,b);
			break;
		case "√":
			raiz(a);
			break;
		}
		
		return String.valueOf(expressao);
	}
	
	
	private double multiplicar(double valorA, double valorB) {
		return valorA * valorB;
	}
	
	
	private double dividir(double valorA, double valorB) {
		return valorA / valorB;
	}
	
	
	private double somar(double valorA, double valorB) {
		return valorA + valorB;
	}
	
	
	private double subtrair(double valorA, double valorB) {
		return valorA - valorB;
	}
	
	
	private double raiz(double valor) {
		return Math.sqrt(valor);
	}


}
