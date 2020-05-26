import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PanelDinamicComponent } from './panel-dinamic.component';

describe('PanelDinamicComponent', () => {
  let component: PanelDinamicComponent;
  let fixture: ComponentFixture<PanelDinamicComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PanelDinamicComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PanelDinamicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
