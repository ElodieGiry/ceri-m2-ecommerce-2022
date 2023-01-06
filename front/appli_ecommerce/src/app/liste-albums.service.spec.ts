import { TestBed } from '@angular/core/testing';

import { ListeAlbumsService } from './liste-albums.service';

describe('ListeAlbumsService', () => {
  let service: ListeAlbumsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ListeAlbumsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
