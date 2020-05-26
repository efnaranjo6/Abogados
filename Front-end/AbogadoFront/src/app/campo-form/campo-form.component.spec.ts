import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampoFormComponent } from './campo-form.component';

describe('CampoFormComponent', () => {
  let component: CampoFormComponent;
  let fixture: ComponentFixture<CampoFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampoFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampoFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
