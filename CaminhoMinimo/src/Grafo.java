import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Pattern;




public class Grafo {

	ArrayList<Vertice> v = new ArrayList();
	ArrayList<Vertice> ordemTopologica = new ArrayList();
	int valorV;
	int matrizDijkstra[][];
	ArrayList<Vertice> n = new ArrayList();
	ArrayList<Vertice> simulaHeap = new ArrayList();

	public void ligaVertices(Vertice v1, Vertice v2, int peso) {
		Aresta a1 = new Aresta(v2, peso);
		v1.arestas.add(a1);
		v1.nVizinhos++;
	}

	public void mostrarGrafo(Vertice v1) {

		if (v1.isVisitado == false) {
			v1.isVisitado = true;
			valorV++;
			v1.tempoVisita = valorV;
			for (int j = 0; j < v1.arestas.size(); j++) {
				mostrarGrafo(v1.arestas.get(j).vizinho);
			}
			valorV++;
			v1.tempoPreto = valorV;
			ordemTopologica.add(0, v1);
		}

	}

	public void inicializaDijkstra() {
		for (int i = 0; i < matrizDijkstra.length; i++) {
			matrizDijkstra[i][0] = 0;
			matrizDijkstra[i][1] = -1;
		}
	}

	public void dijkstra(Vertice inicial) {
		inicializaDijkstra();
		inicial.dist = 0;
		int menorDist = 2147483647;
		int cont = 0;
		v.get(inicial.id).dist = 0;
		while (cont < v.size()) {
			Vertice aux = null;
			for (int i = 0; i < v.size(); i++) {
				if (!n.contains(v.get(i))) {
					if (v.get(i).dist < menorDist) {
						aux = v.get(i);
						menorDist = v.get(i).dist;
					}
				}else {
					continue;
				}
			}

			n.add(aux);
			cont++;
			//System.out.println(aux.id);
			for (int i = 0; i < aux.arestas.size(); i++) {
				if (aux.arestas.get(i).vizinho.dist == 2147483647) {
					//System.out.println(aux.arestas.get(i).vizinho.id);
					aux.arestas.get(i).vizinho.dist = aux.dist + aux.arestas.get(i).peso;
					aux.arestas.get(i).vizinho.pai = aux.id;
					matrizDijkstra[aux.arestas.get(i).vizinho.id][0] = aux.arestas.get(i).peso + aux.dist;
					matrizDijkstra[aux.arestas.get(i).vizinho.id][1] = aux.id;
					v.get(aux.arestas.get(i).vizinho.id).dist = aux.arestas.get(i).peso + aux.dist;
				} else {
					if (aux.arestas.get(i).vizinho.dist > (aux.dist + aux.arestas.get(i).peso)) {
						//System.out.println(aux.arestas.get(i).vizinho.id);
						aux.arestas.get(i).vizinho.dist = aux.dist + aux.arestas.get(i).peso;
						aux.arestas.get(i).vizinho.pai = aux.id;
						matrizDijkstra[aux.arestas.get(i).vizinho.id][0] = aux.arestas.get(i).peso + aux.dist;
						matrizDijkstra[aux.arestas.get(i).vizinho.id][1] = aux.id;
						v.get(aux.arestas.get(i).vizinho.id).dist = aux.arestas.get(i).peso + aux.dist;
					}
				}
				
			}
			menorDist = 2147483647;

		}
	}

	public static void main(String[] args) {
		Scanner n = new Scanner(System.in);
		String qntVerticeAresta = n.nextLine();
		String[] items = qntVerticeAresta.split(" ");
		int qntVertice = Integer.parseInt(items[0]);
		Scanner m = new Scanner(System.in);
		int qntAresta = Integer.parseInt(items[1]);
		Grafo grafo = new Grafo();
		for(int i=0; i < qntVertice; i++) {
			grafo.v.add(new Vertice(i));
		}
		
		for (int i = 0; i < qntAresta; i++) {
			String qntVVP = n.nextLine();
			items = qntVVP.split(" ");
			int vertice1 = Integer.parseInt(items[0]);
			int vertice2 = Integer.parseInt(items[1]);
			int peso = Integer.parseInt(items[2]);
			Vertice v1 = grafo.v.get(vertice1-1);
			Vertice v2 = grafo.v.get(vertice2-1);
			grafo.ligaVertices(v1, v2, peso);
		}

		grafo.matrizDijkstra = new int[grafo.v.size()][2];
		grafo.dijkstra(grafo.v.get(0));
		String s="";
		int aux = grafo.v.size()-1;
		int cont=0;
		for (int i = 0; i < grafo.v.size() ; i++) {
			cont++;
			s += "\n"+(grafo.matrizDijkstra[aux][1]+1);
			aux = aux - 1;
			if(aux==1)
				break;
		}
		String invertida = new StringBuilder(s).reverse().toString();
		System.out.println(cont);
		System.out.println(invertida);
		


	}
}