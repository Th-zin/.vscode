#include <stdio.h>
#include "string.h"

struct Aluno
{
    char nome[50];
    int idade;
    int matricula;
    char curso[30];
};

int main()
{
    int i;
    struct Aluno alunos[3];

    strcpy(alunos[0].nome, "Sergio Silva");
    alunos[0].idade = 16;
    alunos[0].matricula = 1001;
    strcpy(alunos[0].curso, "Matemática");

    strcpy(alunos[1].nome, "Julia Pereira");
    alunos[1].idade = 17;
    alunos[1].matricula = 1002;
    strcpy(alunos[1].curso, "Física");

    strcpy(alunos[2].nome, "João Souza");
    alunos[2].idade = 18;
    alunos[2].matricula = 1003;
    strcpy(alunos[2].curso, "Química");

    printf("===Dados dos Alunos Cadastrado===\n");
    for (i = 0; i < 3; i++)
    {
        printf("Nome: %s\n", alunos[i].nome);
        printf("Idade: %d\n", alunos[i].idade);
        printf("Matrícula: %d\n", alunos[i].matricula);
        printf("Curso: %s\n", alunos[i].curso);
        printf("-----------------------------\n");
    }

    return 0;
}
