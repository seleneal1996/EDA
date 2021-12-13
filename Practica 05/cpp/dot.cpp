/* GRAFICA */
/*@Author: Alejandra Bustinza*/
	void textDot (Node *t,ofstream &os) const{
	
	void textDot (Node *parent, Node *child ,ofstream &os) const{
		char com = '"';
		if(t!=NULL) {
			if(t->child != NULL){
			   os<<com<<"["<<parent->data<<" "<<child->data<<"]"<<com<<"->"<<com<<"["<<t->child<<" "<<t->parent<"]"<<com<<";\n";
			   textDot(child->data,os);
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
