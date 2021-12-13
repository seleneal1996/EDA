/* GRAFICA */
/*@Author: Alejandra Bustinza*/
	void textDot (Node *t,ofstream &os) const{
		char com = '"';
		if(t!=NULL) {
			if(t->child != NULL){
			   os<<com<<"["<<t->child<<" "<<t->child<<"]"<<com<<"->"<<com<<"["<<t->child<<" "<<t->child<"]"<<com<<";\n";
			   textDot(t->,os);
			   }
			/*if(t-> .. !=NULL){
				os<<com<<"["<<t->child<" "<<t->child<<"]"<<com<<"->"<<com<<"["<<t->child<<" "<<t->child<<"]"<<com<<";\n";
				textDot(t->right,os);
			}
			//textDot(t->child,os);
			//textDot(t->child,os);*/
			}
		}
	}
			
	void archiveDot(Node *t) const{
			ofstream Tree;
			Tree.open("Mtree.dot");
			Tree<<"digraph Mtree { \n";
				if(t !=NULL) {
					textDot(t,Tree);
				}Tree<<"} \n";
			Tree.close();
	}

	void pngDot(){
		system("dot -Tpng Mtree.dot -o Mtree.png");
		system("Mtree.png &" );
	}
