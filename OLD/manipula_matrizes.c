#include <stdio.h>

#define LINHAS  3
#define COLUNAS 3



void imprime_matriz(int matriz[LINHAS][COLUNAS]){
  int i;
  int j; 
  for(i = 0; i < LINHAS; i++)
    {
      for(j = 0; j < COLUNAS; j++)
      {
        printf("%4d ",matriz[i][j]);
      }
      printf("\n");
    }
}


int** le_matriz(FILE* file, int matriz[LINHAS][COLUNAS] ){
  int i;
  int j; 
  int erro = 0;
    for(i = 0; i < LINHAS; i++)
    {
      for(j = 0; j < COLUNAS; j++)
      {
        if( !fscanf(file,"%d",&matriz[i][j]) )
        {
          erro = 1;
          printf("Erro a o ler a entrada (%d,%d) da matriz\n",i,j);
          break;
        }
      }
      if( erro )
        break;
    }

    imprime_matriz(matriz);
    return matriz;
}

void le_arq() {
  FILE* file;
  file = fopen("mat.txt","rt"); 
  int MA1[LINHAS][COLUNAS];
  int MA2[LINHAS][COLUNAS];

  if( file )
  {
    printf("MA1\n");
    le_matriz(file, MA1);
    printf("MA2\n");
    le_matriz(file, MA2);

    fclose(file);
  }
  else
  {
    printf("Erro ao abrir o arquivo texto para leitura");
  }
}

int escreve_matriz (FILE* file, int matriz[LINHAS][COLUNAS] ) {
  int i;
  int j; 
  for(i = 0; i < LINHAS; i++)
    {
      for(j = 0; j < COLUNAS; j++)
      {
        fprintf(file,"%4d ",matriz[i][j]);
      }
      fprintf(file,"\n");
    }
    return 0;
}

void escreve_arq(int MA1[LINHAS][COLUNAS], int MA2[LINHAS][COLUNAS]){
  FILE* file;
  file = fopen("mat.txt","wt"); 
  if( file )
  {
    escreve_matriz(file, MA1);
    escreve_matriz(file, MA2);

    fclose(file);
  }
  else
  {
    printf("Erro ao abrir o arquivo texto para escrita");
  }
}

int main(int argc,char *argv[])
{
 
  int nr;
  int nw;
  int erro;
 

  int MA1[LINHAS][COLUNAS] = {{1,1,1},{2,2,2},{3,3,3}};
  int MA2[LINHAS][COLUNAS] = {{1,2,4},{3,4,6},{5,6,7}};

  /*  Abre o arquivo e escreve matriz */
  escreve_arq(MA1, MA2);
  le_arq();

  return 0;
}

/*



int multiplica_matriz()
{ int linha;
  int coluna;
  int i;
  int somaprod;
  int mat1[3][3]={{1,2,3},{4,5,6},{7,8,9}};
  int mat2[3][3]={{1,0,0},{0,1,0},{0,0,1}};
  int mat3[3][3];
  int M1L=3, M1C=3, M2L=3, M2C=3;
  for(linha=0; linha<M1L; linha++) 
    for(coluna=0; coluna<M2C; coluna++){ 
      somaprod=0; 
      for(i=0; i<M1L; i++){
        somaprod+=mat1[linha][i]*mat2[i][coluna]; 
      }
      mat3[linha][coluna]=somaprod; 
    } 
  // 
  //imprime mat3 
  // 
  for(linha=0; linha<M1L; linha++){ 
    for(coluna=0; coluna<M2C; coluna++) 
      printf("%d ", mat3[linha][coluna]); 
    printf("\n"); 
  }
  system("PAUSE");      
  return 0;
}

int main(int argc,char *argv[]){


}*/