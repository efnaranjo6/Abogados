import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  titleA: string ;
  title = 'AbogadoFront';
  Abogados=[]

  constructor(
    private _http: HttpClient){}
    

  ngOnInit(){
    this._http.get('http://127.0.0.1:8000/Persona/')
    .subscribe((datos: any[]) => this.Abogados = datos )
  }

 

}
