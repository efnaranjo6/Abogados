import { Component, OnInit,Input } from '@angular/core';

@Component({
  selector: 'app-servicios',
  templateUrl: './servicios.component.html',
  styleUrls: ['./servicios.component.css']
})
export class ServiciosComponent implements OnInit {
  @Input() titleA : string;
  constructor() { }

  ngOnInit(): void {
  }

}
