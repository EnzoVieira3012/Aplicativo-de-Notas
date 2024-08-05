class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        self.notes.append(Note(title, content))
        print(f"Nota '{title}' adicionada com sucesso.")

    def edit_note(self, index, new_title, new_content):
        if 0 <= index < len(self.notes):
            self.notes[index].title = new_title
            self.notes[index].content = new_content
            print(f"Nota '{new_title}' editada com sucesso.")
        else:
            print("Índice inválido.")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            removed_note = self.notes.pop(index)
            print(f"Nota '{removed_note.title}' removida com sucesso.")
        else:
            print("Índice inválido.")

    def list_notes(self):
        if not self.notes:
            print("Nenhuma nota disponível.")
        else:
            print("\nNotas:")
            for i, note in enumerate(self.notes):
                print(f"{i}. {note.title}")

    def view_note(self, index):
        if 0 <= index < len(self.notes):
            note = self.notes[index]
            print(f"\nTítulo: {note.title}\nConteúdo:\n{note.content}")
        else:
            print("Índice inválido.")

def main():
    manager = NoteManager()

    while True:
        print("\n1. Adicionar Nota")
        print("2. Editar Nota")
        print("3. Excluir Nota")
        print("4. Listar Notas")
        print("5. Ver Nota")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            title = input("Digite o título da nota: ")
            content = input("Digite o conteúdo da nota: ")
            manager.add_note(title, content)
        elif choice == '2':
            manager.list_notes()
            index = int(input("Digite o índice da nota a ser editada: "))
            new_title = input("Digite o novo título da nota: ")
            new_content = input("Digite o novo conteúdo da nota: ")
            manager.edit_note(index, new_title, new_content)
        elif choice == '3':
            manager.list_notes()
            index = int(input("Digite o índice da nota a ser excluída: "))
            manager.delete_note(index)
        elif choice == '4':
            manager.list_notes()
        elif choice == '5':
            manager.list_notes()
            index = int(input("Digite o índice da nota a ser visualizada: "))
            manager.view_note(index)
        elif choice == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
