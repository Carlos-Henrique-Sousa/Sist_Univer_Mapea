import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule  // Importar HttpClient para fazer requisições HTTP
  ],
  providers: [],
  bootstrap: [AppComponent] // O componente principal da aplicação
})
export class AppModule { }
