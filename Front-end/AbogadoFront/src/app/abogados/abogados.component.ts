import { Component, OnInit,Input } from '@angular/core';

@Component({
  selector: 'app-abogados',
  templateUrl: './abogados.component.html',
  styleUrls: ['./abogados.component.css']
})
export class AbogadosComponent implements OnInit {
  @Input("data") abogado :any
 
  constructor() { }

  ngOnInit(): void {
  }

}
