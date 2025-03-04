import { Component, AfterViewInit, ElementRef, ViewChildren, QueryList, HostListener } from '@angular/core';
import { debounceTime } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements AfterViewInit {
  @ViewChildren('section') sections!: QueryList<ElementRef>;
  @ViewChildren('icon') icons!: QueryList<ElementRef>;
  @ViewChildren('dot') dots!: QueryList<ElementRef>;

  ngAfterViewInit() {
    this.updateSidebar();
  }

  @HostListener('window:scroll', [])
  onWindowScroll() {
    debounceTime(100);
    this.updateSidebar();
  }

  updateSidebar() {
    this.sections.forEach((section, index) => {
      const rect = section.nativeElement.getBoundingClientRect();
      const isVisible = rect.top <= window.innerHeight && rect.bottom >= 0;

      const iconElement = this.icons.get(index)?.nativeElement;
      const dotElement = this.dots.get(index)?.nativeElement;

      if (iconElement) {
        iconElement.classList.toggle('active', isVisible);
      }

      if (dotElement) {
        dotElement.style.display = isVisible ? 'none' : 'block';
      }
    });
  }
}