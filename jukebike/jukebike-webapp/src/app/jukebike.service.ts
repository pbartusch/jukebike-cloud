import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { environment } from '../environments/environment';

/**
 * model for the service (e.g. search results)
 */

export class JukeTrack {
  name: string;
  uri: string;
}

/**
 * example:
 * {'status': 'OK', 'queuePosition': 2, 'secondsToWait': 105}
 */
export class WishConfirmation {
  status: string;
  queuePosition: number;
  secondsToWait: number;
}

/**
 * service
 */

@Injectable({
  providedIn: 'root'
})
export class JukeBikeService {

  currentWish: JukeTrack = null
  currentConfirmation: WishConfirmation = null

  // TODO make dynamic / configurable
  private API_ROOT = ""
  private readonly CALL_SEARCH = "/search"
  private readonly CALL_WISH_TRACK = "/wish-track"
  private API_HEADERS = new HttpHeaders()

  constructor(
    private http: HttpClient
  ) {
    this.API_HEADERS.set('Content-Type', 'application/json; charset=utf-8')
    this.API_ROOT = environment.API_ROOT
  }

  searchSong(input: string): Promise<Array<JukeTrack>> {
    console.log('In JukeBikeService :: searchSong :: input = ' + input)
    let searchParams = new HttpParams().set("input", input);
    return this.http
      .get(this.API_ROOT + this.CALL_SEARCH,
        {
          params:searchParams,
          headers:this.API_HEADERS
        })
      .toPromise()
      .then(resp => resp as Array<JukeTrack>)
  }

  wishTrack(trackUri: string, username: string): Promise<WishConfirmation> {
    return this.http
      .post(this.API_ROOT + this.CALL_WISH_TRACK,
        JSON.stringify({
            'trackUri': trackUri,
            'username': username
        }),
        {
          headers:this.API_HEADERS
        })
      .toPromise()
      .then(resp => resp as WishConfirmation)
  }
}
