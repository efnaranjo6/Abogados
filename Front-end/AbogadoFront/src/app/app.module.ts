import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { ButtonComponent } from './button/button.component';
import { PanelServicesComponent } from './panel-services/panel-services.component';
import { FooterComponent } from './footer/footer.component';
import { ImagesComponent } from './images/images.component';
import { CampoFormComponent } from './campo-form/campo-form.component';
import { PanelDinamicComponent } from './panel-dinamic/panel-dinamic.component';
import { HomeComponent } from './home/home.component';
import { ServiciosComponent } from './servicios/servicios.component';
import { AbogadosComponent } from './abogados/abogados.component';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    ButtonComponent,
    PanelServicesComponent,
    FooterComponent,
    ImagesComponent,
    CampoFormComponent,
    PanelDinamicComponent,
    HomeComponent,
    ServiciosComponent,
    AbogadosComponent,
   
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
