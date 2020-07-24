import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WishSongComponent } from './wish-song.component';

describe('WishSongComponent', () => {
  let component: WishSongComponent;
  let fixture: ComponentFixture<WishSongComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WishSongComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WishSongComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
