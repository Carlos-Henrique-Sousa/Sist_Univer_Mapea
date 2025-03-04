import { Component } from '@angular/core';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  imports: [FontAwesomeModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  sections!: NodeListOf<HTMLElement>;
  
  ngAfterViewinit() {
    
  }
 }
