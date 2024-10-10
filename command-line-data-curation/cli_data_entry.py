from rich.console import Console
from rich.table import Table

console = Console()
console.print("Here is some initial data:", style="bold cyan")

table = Table(title="Albums to listen to")
table.add_column("Artist Name", style="red", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Genre")
table.add_column("Release Year")
table.add_row("Todd Rundgren", "Something/Anything", "Power Pop, Rock", "1972")
table.add_row("Joe Farrel", "Moon Germs", "Jazz(Post-bop/Fusion)", "1973")
table.add_row("The American Analog Set","The Fun of Watching Fireworks", "Space Age Revival, Post-Rock", "1996")

console.print(table)
console.print("\n[bold cyan]Now I want you to enter your preferred movies:[/bold cyan]")

while True:
    reps = input("Enter the number of albums you want to enter: ")

    for i in range(int(reps)):
        while True:
            artist = input("Enter the artist of the album: ")
            title = input("Enter the name of the album: ")
            genre = input("Enter the genre of the album: ")
            release_year = input("Enter the release year of the album: ")
            
            console.print(f"\n[bold]You entered:[/bold]\nArtist: {artist}\nTitle: {title}\nGenre: {genre}\nRelease Year: {release_year}")
            confirm = input("Is this correct? (yes/no): ")
            
            if confirm.lower() == 'yes':
                table.add_row(artist, title, genre, release_year)
                break
            else:
                console.print("[bold red]Let's try again.[/bold red]")
    
    console.print(table)
    
    reset = input("Do you want to enter more albums? (yes/no): ")
    if reset.lower() != 'yes':
        break
   
with open("album_list.txt", "w") as file:
    with console.capture() as capture:
        console.print(table)
    file.write(capture.get())