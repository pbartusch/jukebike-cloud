import { TestBed } from '@angular/core/testing';

import { JukeBikeService } from './jukebike.service';

describe('JukeBikeService', () => {
  let service: JukeBikeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(JukeBikeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
