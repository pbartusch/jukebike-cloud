import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfirmWishComponent } from './confirm-wish.component';

describe('ConfirmWishComponent', () => {
  let component: ConfirmWishComponent;
  let fixture: ComponentFixture<ConfirmWishComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConfirmWishComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfirmWishComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
